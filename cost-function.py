import sys
import math
import numpy
from scipy.stats import norm

def zScore(confidence_level):
    '''This function is used to calcualte z-score from confidence level'''
    #z-score list 
    z_list = {
        0.90: 1.645,
        0.91: 1.695,
        0.99: 2.576,
        0.97: 2.17,
        0.94: 1.881,
        0.93: 1.812,
        0.95: 1.96,
        0.98: 2.326,
        0.96: 2.054,
        0.92: 1.751
    }
    alpha = 1 - (confidence_level)
    if confidence_level in z_list:
        z = z_list[confidence_level]
    else:
        z = norm.ppf(1 - (alpha/2))
    return z


def sampleSizeCalc(population_size, confidence_level, error_bound, sigma=.5):
    '''This function is used to identify sample size from error_bound.
    sigma: is standard deviation of the population.'''
    N = population_size
    M = error_bound
    z = zScore(confidence_level)
   
    #sample size
    print z, N, M, sigma 
    sample_size = int(math.ceil((z**2 * sigma**2)/(M**2)))
    return sample_size

def latencyCalc(input_size):
    '''This function estimate the latency from size of cross-product.
    For SE group TU Dresden cluster: latency = 27.86*input_size + 29.45.
    Input size unit is million [M] and latency unit is seconds [s]'''
    latency = 27.86*input_size + 121.45 #29.45 + 36 + 28 + 28
    return latency

def sampleSize(latency):
    sample_size = int((latency - 118)/(4.15989409766e-09))
    return sample_size
    
def main():
    sample_sz = 0
    population_sz = 173608888896
    confidence_level = 0.95
    error_bound = 0.05 #2.0
    #sigma = 20#30911
    #sample_sz = sampleSizeCalc(population_sz, confidence_level, error_bound, sigma)
    #sample_sz = int(173608888896/100/1000000) #1%
    #latency = latencyCalc(float(sample_sz)/1000000) #input size in Million
    #f = float(sys.argv[1])
    #sample_sz = population_sz*f
    latency = float(sys.argv[1])
    sample_sz = sampleSize(latency) 
    sampling_fraction = float(sample_sz)/173608888896.0

    #print "Sample Size: %d, Latency: %f" % (sample_sz, latency)
    print "Sample fraction: %f, Latency: %d [seconds]" % (sampling_fraction, latency)

if __name__ == "__main__":
    main() 
