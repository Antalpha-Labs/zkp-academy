from ec import (default_ec, G1Generator, G2Generator)
from poly_utils import PrimeField
import random
from fft import fft
from pairing import ate_pairing
from fields import Fq
class PolyCommit:
    def __init__(self):
        self.modulus = default_ec.n
        self.pf = PrimeField(self.modulus)
        self.secret = random.randint(0, self.modulus -1)
        self.G1 = G1Generator()
        self.G2 = G2Generator()
        self.G1Vec = []
        self.G2Vec = []
    
    def getSetupG1Vec(self, length):
        for i in range(len(self.G1Vec), length):
                self.G1Vec.append(self.G1 * (self.secret ** i))
        return self.G1Vec[0:length]

    def getSetupG2Vec(self, length):
        for i in range(len(self.G2Vec), length):
                self.G2Vec.append(self.G2 * (self.secret ** i))
        return self.G2Vec[0:length]
    
    # g: root of unity 
    def getCommitment(self, evals, g):
        coeffs = fft(evals, self.modulus, g, True)
        g1vec = self.getSetupG1Vec(len(coeffs))
        return sum( s * c for s,c in zip(g1vec, coeffs))
    
    def getCommitmentByCoeffs(self, coeffs):
        g1vec = self.getSetupG1Vec(len(coeffs))
        return sum( s * c for s,c in zip(g1vec, coeffs))
    def getG2CommitmentByCoeffs(self, coeffs):
        g2vec = self.getSetupG2Vec(len(coeffs))
        return sum( s * c for s,c in zip(g2vec, coeffs))

    def getSingleProofAtEvalIdx(self, evals, g, idx):
        # qx = (fx - y0)/ (x = x0)
        coeffs = fft(evals, self.modulus, g, True)
        x0 = self.pf.exp(g, idx)
        y0 = evals[idx]
        coeffs[0] = coeffs[0] - y0
        qx = self.pf.div_polys(coeffs, [self.modulus - x0, 1])
        g1Vec = self.getSetupG1Vec(len(qx))
        return x0, y0, sum( s * c for s,c in zip(g1Vec, qx))
    
    def verifySingleProof(self, commitment, proof, x0, y0):
        pairLeft = ate_pairing(commitment + (self.G1 * y0).negate(), self.G2)
        g2 = self.getSetupG2Vec(2)[1]  # g2 * secret
        pairRight = ate_pairing(proof,  g2 + (self.G2 * x0).negate())
        assert pairLeft == pairRight, "Pairing check failed"

import unittest
class Test(unittest.TestCase):
    def test_single_proof(self):         
        pc = PolyCommit()
        evals = [101,12,13,24]
        G = pc.pf.exp(7, (pc.pf.modulus -1) // 4)
        commitment = pc.getCommitment(evals, G)
        print("poly commitment:", commitment)

        # random
        idx = random.randint(0, len(evals)-1)
        x0, y0, evaluation_proof = pc.getSingleProofAtEvalIdx(evals, G, idx)
        print("evaluation point:", idx, x0, y0)
        print("evaluation proof:", evaluation_proof)

        pc.verifySingleProof(commitment, evaluation_proof, x0, y0)
        print("proof verification check passed")

    def test_multi_openning_proofs(self):
        pc = PolyCommit()
        G = pc.pf.exp(7, (pc.pf.modulus -1) // 4)
        f1_evals = [1,2,3,4]
        f2_evals = [4,5,6,7]
        commit_f1 = pc.getCommitment(f1_evals, G)
        commit_f2 = pc.getCommitment(f2_evals, G)

        ## Verifier send random number v
        idx = random.randint(0, max(len(f1_evals), len(f2_evals)) -1)

        ## Prover calculate q(x) = q1(x) + v * q2(x)
        x0, y1_0, q1_x = pc.getSingleProofAtEvalIdx(f1_evals, G, idx)
        _, y2_0, q2_x = pc.getSingleProofAtEvalIdx(f2_evals, G, idx)
        proof = q1_x + q2_x * x0
        ## pairing check
        cg = commit_f1 + commit_f2 * x0
        yg = y1_0 + y2_0 * x0
        pc.verifySingleProof(cg,proof,x0, yg)
        print("multi opening proof check passed")
    
    def test_shplonk(self):
        # shplonk
        pc = PolyCommit()
        f1_evals = [10,20,30,40]
        f2_evals = [4,5,6,7]
        G = pc.pf.exp(7, (pc.pf.modulus -1) // 4)
        idxs_1 = [0,1]
        idxs_2 = [0,1,2]

        ## calculate ri(x)
        xs_1 = [pc.pf.exp(G, idx) for idx in idxs_1]
        ys_1 = [f1_evals[idx] for idx in idxs_1]
        rx_1 = pc.pf.lagrange_interp(xs_1, ys_1)

        xs_2 = [pc.pf.exp(G, idx) for idx in idxs_2]
        ys_2 = [f2_evals[idx] for idx in idxs_2]
        rx_2 = pc.pf.lagrange_interp(xs_2, ys_2)

        ## bind all polynomials of fi(x)
        gama = pc.pf.exp(G, random.randint(0, 4))

        print("r1_coeffs:", pc.pf.degree(rx_1))
        print("r2_coeffs:", pc.pf.degree(rx_2))

        # Prover makes the bound-together quotient polynomial
        # zx_1 = pc.pf.lagrange_interp(xs_1, [0]*len(xs_1))
        zx_1 = pc.pf.zpoly(xs_1)
        # zx_2 = pc.pf.lagrange_interp(xs_2, [0]*len(xs_2))
        zx_2 = pc.pf.zpoly(xs_2)
        print("zx_1_coeffs:", pc.pf.degree(zx_1))
        print("zx_2_coeffs:", pc.pf.degree(zx_2))
        ztx = zx_2
        fx_1 = fft(f1_evals, pc.modulus, G, True)
        fx_2 = fft(f2_evals, pc.modulus, G, True)
        print("fx_1_coeffs:", pc.pf.degree(fx_1))
        print("fx_1_coeffs:", pc.pf.degree(fx_2))
        hx_1 = pc.pf.div_polys(pc.pf.sub_polys(fx_1, rx_1), zx_1)
        hx_2 = pc.pf.div_polys(pc.pf.sub_polys(fx_2, rx_2), zx_2)
        print("hx_1_coeffs:", pc.pf.degree(hx_1))
        print("hx_2_coeffs:", pc.pf.degree(hx_2))
        hx = pc.pf.add_polys(hx_1,  pc.pf.mul_by_const(hx_2, gama))
        print("hx_coeffs:", pc.pf.degree(hx))

        ## proofs
        fx_1_commit = pc.getCommitmentByCoeffs(fx_1) # c1
        fx_2_commit = pc.getCommitmentByCoeffs(fx_2) # c2
        rx_1_commitG1 = pc.getCommitmentByCoeffs(rx_1)
        rx_2_commitG1 = pc.getCommitmentByCoeffs(rx_2)
        zt_div_z1_commitG2 = pc.getG2CommitmentByCoeffs(pc.pf.div_polys(ztx, zx_1))
        zt_div_z2_commitG2 = pc.getG2CommitmentByCoeffs(pc.pf.div_polys(ztx, zx_2))
        ztx_commitG2 = pc.getG2CommitmentByCoeffs(ztx)
        proof = pc.getCommitmentByCoeffs(hx)

        ## verfier checks the proofs
        pair_left_1 = ate_pairing(fx_1_commit +  rx_1_commitG1.negate(), zt_div_z1_commitG2)
        pair_left_2 = ate_pairing(
            (fx_2_commit +  rx_2_commitG1.negate())*gama, 
            zt_div_z2_commitG2
            )
        pair_left = pair_left_1 * pair_left_2
        pair_right = ate_pairing(proof, ztx_commitG2)
        assert pair_left == pair_right, "pairing check failed"




if __name__ == '__main__':
    unittest.main(verbosity=2)   # run all test cases