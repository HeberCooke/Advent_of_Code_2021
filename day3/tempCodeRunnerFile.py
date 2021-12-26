        ones,zeros = find_bit(data, position)

        print('Position ',position)
        print('ones ', ones)
        print('zeros ', zeros)
        
        if ones >= zeros:
            data = add_to_list(data,position,True)
        else:
            data = add_to_list(data, position, False)
        print(data)
        
        position += 1