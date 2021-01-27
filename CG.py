import gpt_2_simple as gpt2

class CovidGenerator():

    def __init__(self):
        pass
        #gpt2.load_gpt2(sess, run_name='run1')

    def generate(self):
        
        '''
        if sess is None:
            print("sess is none")
            sess = gpt2.start_tf_sess()
            gpt2.load_gpt2(sess, run_name='run1')
        else:
            print("sess is not none")
            sess = gpt2.start_tf_sess()
            gpt2.load_gpt2(sess, run_name='run1')    
        '''
        sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(sess, run_name='run1')

        gpt_response = gpt2.generate(sess,
              length=250,
              temperature=0.7,
              truncate='<|endoftext|>',
              nsamples=1,
              batch_size=1,
              return_as_list=True
              )[0]  
        return gpt_response   
'''
        print(gpt_response)
        splitted_text = gpt_response.split(">")

        print(splitted_text)

        if len(splitted_text) > 1:
            print (splitted_text[1])
            answer = splitted_text[1]
        else:
            answer = splitted_text[0]
'''
         
