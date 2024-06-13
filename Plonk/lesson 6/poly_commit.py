from ec import (default_ec, G1Generator, G2Generator)
from poly_utils import PrimeField
import random
from fft import fft
from pairing import ate_pairing
class PolyCommit:
    def __init__(self):
        self.modulus = default_ec.n
        self.pf = PrimeField(self.modulus)
        self.secret = random.randint(0, self.modulus -1)
        self.G1 = G1Generator()
        self.G2 = G2Generator()
        self.G1Vec = []
    
    def getSetupG1Vec(self, length):
        for i in range(len(self.G1Vec), length):
                self.G1Vec.append(self.G1 * (self.secret ** i))
        return self.G1Vec[0:length]
    
    # g: root of unity 
    def getCommitment(self, evals, g):
        coeffs = fft(evals, self.modulus, g, True)
        g1vec = self.getSetupG1Vec(len(coeffs))
        return sum( s * c for s,c in zip(g1vec, coeffs))

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
        pairRight = ate_pairing(proof, self.G2 * self.secret + (self.G2 * x0).negate())
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




if __name__ == '__main__':
    unittest.main(verbosity=2)   # run all test cases