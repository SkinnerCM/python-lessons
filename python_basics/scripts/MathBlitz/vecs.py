"""
Created on Sat Jan 11 18:55:29 2025

@author: Colin
"""
class Vec:
    
    def __init__(self, *args):
        
        self.elements = tuple(args)
        
    def __repr__(self):
        return(f"<{','.join(map(str, self.elements))}>")
    
    def __len__(self):
        return len(self.elements)
    
    def __getitem__(self, index):
        return self.elements[index]

    def __add__(self, other):
        if not isinstance(other, Vec):
            raise TypeError("Can only add Vec to Vec.")
            
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must be the same length for addition.")
            
        return Vec(*(a+b for a,b in zip(self.elements, other.elements)))
    
    def __sub__(self, other):
        if not isinstance(other, Vec):
            raise TypeError("Can only subtract Vec from Vec.")
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must be the same length for subtraction.")
        
        return Vec(*(a-b for a,b in zip(self.elements, other.elements)))
    
    def dot(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must be the same length.")
        
        dotprod = 0
        
        for a,b in zip(self.elements, other.elements):
            dotprod+=a*b

        return dotprod

    def magnitude(self):
        from math import sqrt
        return sqrt(self.dot(self))