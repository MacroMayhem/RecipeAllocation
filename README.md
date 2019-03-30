# RecipeAllocation

## Contents

1. [Introduction](#introduction)
2. [Algorithm](#algorithm)
3. [Project Structure](#project-structure)
4. [How To Run](#how-to-run)


### Introduction

The project contains the implementation of recipe allocation algorithm for the default orders. It return a **Boolean** value representing if the constraints imposed are satisfied or not.

### Algorithm

Greedy Allocation: Utilizes the recipes for which the stock is maximum. The detailed working is listed below

1. We create a *max-Priority* queue for recipes based on the stock
2. We create another *max-Priority* queue for orders based on the number of recipes required.
3. For each order with `k` required recipes we select the top `k` recipes in stock from the earlier created priority queue. 
4. We reduce the count of each of the `k` recipes by the number of portions required for the order and push it back in the queue
5. We reduce the order count by 1 and place it back in the order queue

**Time Complexity** `O(nlog(a)+nlog(b)), where n is the number of orders, a is the number of unique recipes in stock, b is the different combinations of portions and recipes`

**Note** it is possible to bring the complexity down to `O(nlog(a))` by using a sorted list instead of a priority queue for orders. However, it is left as future work as the value of `b` is very small.
 
 ### Project Structure
 
    .
    ├── data                   # JSON files
    ├── source                 # Implementation of classes such as Recipes, Allocator etc.
    ├── utility                # Utility functions which can be used across the app
    ├── Dockerfile             # Dockerfile containing the docker instructions to set up the environment
    └── README.md
  
### How To Run
We provide *2* ways to run the algorithm. First one uses **Docker** and the second one requires **python** installation. 

##### [DOCKER]
Firstly, navigate to the `$ROOT` of the project. The project structre at `$ROOT` is displayed [above](#project-structure)

Execute the command to build the image

`docker build -t recipe_allocation .`

Next, we need to run the image inside the container by

`docker run -it recipe_allocation`

**Return** True or False depending if the constraints were met or not

In order to run on different jsons one can either edit the `CMD` fields in the dockerfile appropriately 
`CMD ["python", "main.py","-p", "./data/","-o","orders.json","-s","stock.json"]`  
or can replace the `stock.json` and `orders.json` in the `$ROOT/data/` folder

##### [STAND-ALONE EXECUTION]Executing the application 
If the user has a working python3 installation. One can easily execute the script
**execution**

`python main.py -p ./data/ -o orders.json -s stock.json`

**help**

`python main.py -h`

**p.s** Prints the boolean value representing if the constraints in the problems are met or not. **True** for constraints being satisfied
**False** otherwise
