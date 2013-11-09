## this script compares  the two text files
## first line of defence is to match the number of lines in the file

def compare_two_files(str_1,str_2):
    print "Comparing starts"
    print"First fetching the number of line"
    with open(str_1) as fin :
        lines = sum (1 for line in fin)
    with open(str_2) as fin_2:
        lines_2 = sum(1 for line in fin_2)

    if(lines== lines_2):
        print "First Line of defence is passed"
    else :
        print "First line of defence is not pased"


compare_two_files("C:\\Users\\sappal\\Desktop\\tushar_test_scripts\\sappal.txt","C:\\Users\\sappal\\Desktop\\tushar_test_scripts\\sappal.txt")
        
    
