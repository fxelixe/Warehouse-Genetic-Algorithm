# Warehouse-Genetic-Algorithm

The second task from the Mathematical Modelling course I take is to solve the problem from HiMCM: The High School Mathematical Contest in Modeling Problem B. The problem asked us to model the number and location of warehouses so that the shipping duration is one day for all across USA, according to the shipping duration maps provided by the official website of UPS. We tried recreating the solution Team 2711 offered, though some changes and alteration are made to fit the data currently provided. Genetic algorithm is an algorithm that reflects the process of natural selection where suitable individuals are chosen for reproduction to produce offspring from the next generation. Our team is able to find the best solution by genetic algorithm using the programming language Python.

The paper is in Indonesian language. Feel free to ask or contact me for translation or explanation.

I do not provide the means to download the shipping map from www.ups.com since the maps they provide change with time. I have provided a few samples of the maps I have downloaded in the images_sample folder.

count_pixel.py is used to count the total number of pixel in a shipping map. The total number of pixel will represent the area of USA and will be used a few times in the next codes.

process_map.py processed the original shipping maps to only contains yellow pixels (representing one day shipping area) and black pixels (representing borders, outlines, and texts). A few samples of them are in the images_convert_sample folder.

genetic_algorithm.py processed the converted images to become an input of a genetic algorithm. By deciding the number of warehouse, population, and interation, genetic algorithm helps find the best generation based on the fitness value. In this case, the fitness value is the proportion of area covered by one day shipping.

stack_map.py create a stacked map based on the result of the best generation received from genetic algorithm. A few samples of them are in the images_area_covered folder.

count_overlap.py counts the proportion of the overlap region, which is represented in shades of green. A few samples of them are in the images_overlap folder.
