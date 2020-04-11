

"""
Agent.py file for Solving Raven's Progressive Matrices
Kabir Abdulmajeed
"""


import numpy as np
from PIL import Image
from PIL import ImageFilter

class Agent:

    def __init__(self):
        pass

    def Solve(self, problem): 

        def integral_images(images):
            images = np.array(images, dtype='float64')[:,:,0]
            integral_images = np.cumsum(np.cumsum(images,0),1)
            return integral_images
        
        if problem.problemType=='2x2':
            inputs = [problem.figures['A'].visualFilename,
                      problem.figures['B'].visualFilename,
                      problem.figures['C'].visualFilename]
            tests =  [problem.figures['1'].visualFilename,
                      problem.figures['2'].visualFilename,
                      problem.figures['3'].visualFilename,
                      problem.figures['4'].visualFilename,
                      problem.figures['5'].visualFilename,
                      problem.figures['6'].visualFilename]
        
        
        
            ### 2x2 SIMPLE RPM AGENT ###
            def intScore(image):
                return np.cumsum(np.cumsum(image, 0), 1).std()
            input_iS = [intScore(np.array(Image.open(item))[:,:,0]) for item in inputs]
            tests_iS = [intScore(np.array(Image.open(item))[:,:,0]) for item in tests]
            solution = np.argmin(np.abs((1.0*input_iS[1]*input_iS[2]/input_iS[0]) - np.array(tests_iS))) + 1
            



        if problem.problemType=='3x3':
            inputs = [problem.figures['A'].visualFilename,
                      problem.figures['B'].visualFilename,
                      problem.figures['C'].visualFilename,
                      problem.figures['D'].visualFilename,
                      problem.figures['E'].visualFilename,
                      problem.figures['F'].visualFilename,
                      problem.figures['G'].visualFilename,
                      problem.figures['H'].visualFilename]
            tests =  [problem.figures['1'].visualFilename,
                      problem.figures['2'].visualFilename,
                      problem.figures['3'].visualFilename,
                      problem.figures['4'].visualFilename,
                      problem.figures['5'].visualFilename,
                      problem.figures['6'].visualFilename,
                      problem.figures['7'].visualFilename,
                      problem.figures['8'].visualFilename]

            ### 3x3 SIMPLE RPM AGENT ###
            def intScore(image):
                return np.cumsum(np.cumsum(image, 0), 1).std()
            input_iS = [intScore(np.array(Image.open(item), dtype='float64')[:,:,0]) for item in inputs]
            tests_iS = [intScore(np.array(Image.open(item), dtype='float64')[:,:,0]) for item in tests]
            solution = np.argmin(np.abs((1.0*input_iS[7]**2/input_iS[6]) - np.array(tests_iS))) + 1    

                          
        return solution
      
    
    
    
    
    
    
    
    
    
    