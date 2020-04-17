# SimpleRPM
AI Algorithm for Solving Ravens Progressive Matrices
![SimpleRPM/rpm.jpg]

This work presents a novel method for solving the Ravens Progressive Matrices (RPM) problem using a visual
heuristics based computational AI framework. The Simple-RPM algorithm is a simplified and efficient method based on
three stages: re-representation - a global contractive transformation, prediction stage, and a matching stage. 
![SimpleRPM/integral_images_scores.png]

In the re-representation phase, an integral score for each image is computed, closely followed by the prediction stage where the
integral score corresponding to the missing RPM element is predicted. 
![SimpleRPM/Simple-RPM.png]

Finally, the predicted integral score is used to find the matching test image in the matching stage. The Simple-
RPM performs above average on the Basic-B and Basic-C RPM problem sets. The adjoining code shows how this Agent can be
implemented in roughly 10 lines of python code.
