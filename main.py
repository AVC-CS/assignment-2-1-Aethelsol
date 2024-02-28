def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    m = int(input())
    f = int(input())
    total = m  + f
    m_perc = (m / (total)) * 100
    f_perc = (f / (total)) * 100 
  

    print (f'The total number of students is {total}')
    #print (f'The percent of men is %d, the percent of women is %d' % (m_perc, f_perc))
    print (f'The percent of men is {m_perc:.2f}')
    print (f'The percent of women is {f_perc:.2f}')    
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
    