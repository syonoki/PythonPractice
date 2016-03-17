# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 13:46:30 2016

@author: ijlee
"""
import Quandl as qd

class QdDataProvider:
    lastCode_ = ""
    authtoken_ = ""
    def __init__(self, authtoken):
        self.authtoken_ = authtoken
    
    def get(self, generator, trimStart = None, trimEnd = None):
        requestCode = generator.generate()
        self.lastCode_ = requestCode  
        if not trimStart is None:
            return qd.get(requestCode, trim_start = trimStart, 
                          trim_end = trimEnd, authtoken=self.authtoken_)
        return qd.get(requestCode, authtoken=self.authtoken_);
                
    def lastRequestedCode(self):
        return self.lastCode_;       
  
class QdRequestGenerator:
    providerCode_ = "";
    def __init__(self):
        pass

    def generate(self):
        pass
        
class ImfRequestGenerator(QdRequestGenerator):
    indicator_ = ""
    countries_ = []    
        
    def __init__(self):
        self.providerCode_ = "ODA"  

    def setCriterias(self, countries, indicator):
        self.countries_ = countries
        self.indicator_ = indicator
        
    def generate(self):
        return [ self.providerCode_ + '/' 
            + c + '_' + self.indicator_ for c in self.countries_]

        
class FrExchangeRateRequestGenerator(QdRequestGenerator):
    dataType_ = "RXI"
    indexType_ = ""
    freq_ = ""    
    countries_ = []       
    
    def __init__(self):
        self.providerCode_ = "FED"
        
    def setCriterias(self, indexType, freq, countries = None):
        self.countries_ = countries
        self.indexType_ = indexType
        self.freq_ = freq
        if countries is None:
            self.countries_ = []
        else:
            self.countries_ = countries
    
    def generate(self):
        return [ self.providerCode_ + '/' 
            + self.dataType_ + '_' 
            + self.indexType_ + '_' 
            + self.freq_ + '_' 
            + c for c in self.countries_]
    
    