from random import randint

population=30
mutation_chance=10


def getScores(s_weight,s_value,s_maxweight,s_gen):
        """
        calculates the scores for the different treasures
        input: weight, value, maxweight (for the bag) and the generation
        output: Scores for each part of the generation containing weight and value for the bag
        """
        s_results=[]

        for i in range(len(s_gen)):
                s_total_mass=0
                s_total_value=0
                
                for j in range(len(s_gen[i])):
                        s_total_mass+=s_gen[i][j]*s_weight[j]
                        s_total_value+=s_gen[i][j]*s_value[j]
                
                if s_total_mass>s_maxweight:
                        s_total_value=0

                
                s_results+=[[s_total_mass,s_total_value]]


        return s_results


def get_super_performer(gsp_gen,gsp_scores):
        """
        Get the highest performing individual in the population
        input: the generation and their scores
        output: the index and score of the highest scoring individual
        """
        gsp_index=0
        gsp_max=0
        for i in range(len(gsp_scores)):
                if gsp_scores[i][1]>gsp_max:
                        gsp_max=gsp_scores[i][1]
                        gsp_index=i
        return gsp_index,gsp_max


def mutant_clone(mc_gen,scores):
        """
        Change the population depending on the highest scoring individual
        input: the generation, their relative scores
        output: A new generation in a list,
                offspring from the highest scoring individual
                with mutations
        """
        mc_individual,mc_maxscore=get_super_performer(mc_gen,scores)
        mc_newgen=[mc_gen[mc_individual].copy() for i in range(population)]
        
        for i in range(len(mc_newgen)):
                
                for j in range(len(mc_newgen[i])):
                        
                        mc_r=randint(0,100)
                        
                        if mutation_chance>mc_r:
                                
                                mc_newgen[i][j]=1-mc_newgen[i][j]
                                   
        return mc_newgen,mc_individual,mc_maxscore






def main():
        weight=[7,2,1,9,11,2,3,4,7,9,10,5,4,2,5,6]
        value=[5,4,7,2,5,4,7,8,9,10,2,6,4,1,8,9]
        maxweight=15
        gen=[[randint(0,1) for i in range(len(weight))] for j in range(population)]
        for i in range(70):
                scores=getScores(weight,value,maxweight,gen)
                gen,individual,maximumscore=mutant_clone(gen,scores)
                print(f"gen#{i+1}",gen[individual],maximumscore)
main()
