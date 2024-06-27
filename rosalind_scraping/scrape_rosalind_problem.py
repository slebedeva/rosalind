import requests
import os
from bs4 import BeautifulSoup
import sys

"""
Example usage: python scrape_rosalind_problem.py https://rosalind.info/problems/tran/

Example output:
    1. Puzzle script: ../puzzles/transitions_and_transversions.py
    2. Puzzle sample input: ../puzzles/sample_data/transitions_and_transversions.txt
"""

def scrape_rosalind_problem(problem_suffix: str):
    """
    This opens a rosalind problem and creates the following template files:
    
    problem_name.py in puzzles - script to write your code into
    problem_name.txt - sample input form the description (fasta)
    
    :param problem_suffix: last part of url address of the puzzle to be scraped, 
                    like "fib" in https://rosalind.info/problems/fib/
    """
    
    # get the name of the dataset
    #problem_suffix = [s for s in url.split('/') if s][-1]
    dataset_name = os.path.join('..', 'data', 'rosalind_' + problem_suffix + '.txt')


    # get the html of the page
    base_url = "https://rosalind.info/problems/"
    response = requests.get(base_url + problem_suffix)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # problem title and file names
    title = soup.find('h1').text.split('\r\n')[0]
    puzzle = title.lower().replace(' ','_')
    file_name = puzzle + '.py'
    sample_data_path = os.path.join('..','puzzles','sample_data',puzzle+'.txt')

    # description text
    ps = soup.find_all("p")
    topics = soup.find('p', class_='topics')
    
    # sample data and answer
    sample_data = soup.find_all('div', class_='codehilite')
    sample = sample_data[0].text
    answer = sample_data[1].text
    
    # write everything to a file
    with open(os.path.join('..','puzzles',file_name), 'w') as f:
        f.write('from rosalind.utils import read_multifasta\n\n')
        # function definition to solve the puzzle
        f.write('def solve_' + puzzle + '(fasta_path):\n')
        # write docstring from description
        f.write('\t"""\n')
        f.write('\t'+title+'\n\n')
        if topics:
            f.write('\t'+topics.text+'\n\n')
        f.writelines(['\t'+p.text+'\n' for p in ps[2:6]])
        f.write('\n')
        f.write('\t'+ps[6].text+'\n')
        f.write('\t'+ps[7].text+'\n')
        f.write('\n\t"""\n\n')
        # Write body of the function: import fasta
        f.write('\t# Import sample sequences\n')
        f.write('\tsequences = read_multifasta(fasta_path)\n\n')
        f.write('\treturn\n')
        f.write('\n\n\n')
        # Write main block and assert expected result
        f.write('if __name__=="__main__":\n')
        f.write('\ttry:\n')
        f.write('\t\tans = str(solve_'+puzzle+'("'+sample_data_path+'"))\n')
        f.write('\t\tcorrect = '+'"'+answer.strip()+'"\n')
        f.write('\t\tassert ans == correct\n')
        f.write('\texcept AssertionError:\n')
        f.write('\t\tprint(f"{ans} is wrong")\n')
        f.write('\tprint("------rosalind problem------")\n')
        f.write('\t' + f'#print(solve_{puzzle}("{dataset_name}"))')
        f.close()    

    # write a sample input file
    with open(sample_data_path, 'w') as t:
        t.write(sample)
        t.close()
    
    

if __name__=="__main__":
    try:
        url = sys.argv[1]
        scrape_rosalind_problem(url)
    except:
        print("Please provide a valid Rosalind suffix (last part of problem url) as the first argument")
