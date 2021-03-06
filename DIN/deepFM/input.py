import numpy as np

class DataInput:
        
    def __init__(self, data, batch_size):

        self.batch_size = batch_size
        self.data = data
        self.epoch_size = len(self.data) // self.batch_size
        if self.epoch_size * self.batch_size < len(self.data):
            self.epoch_size += 1
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.i == self.epoch_size:
            raise StopIteration

        ts = self.data[self.i * self.batch_size : min((self.i+1) * self.batch_size, len(self.data))]
        self.i += 1

        u, i, y, sl = [], [], [], []
        for t in ts:
            u.append(t[0])    # userId
            i.append(t[2])    # target
            y.append(t[3])    # label - 0 or 1
            sl.append(len(t[1])) # history_
        max_sl = max(sl)

        hist_i = np.zeros([len(ts), max_sl], np.int64)

        k = 0
        for t in ts:
            for l in range(len(t[1])):
                hist_i[k][l] = t[1][l]
            k += 1

        return self.i, (u, i, y, hist_i, sl)


class DataInputTest:
    def __init__(self, data, batch_size):

        self.batch_size = batch_size
        self.data = data
        self.epoch_size = len(self.data) // self.batch_size
        if self.epoch_size * self.batch_size < len(self.data):
            self.epoch_size += 1
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.i == self.epoch_size:
            raise StopIteration

        ts = self.data[self.i * self.batch_size : min((self.i+1) * self.batch_size,len(self.data))]
        self.i += 1

        u, i, j, sl = [], [], [], []
        for t in ts:
            u.append(t[0])
            i.append(t[2][0])
            j.append(t[2][1])
            sl.append(len(t[1]))
        max_sl = max(sl)

        hist_i = np.zeros([len(ts), max_sl], np.int64)

        k = 0
        for t in ts:
            for l in range(len(t[1])):
                hist_i[k][l] = t[1][l]
            k += 1

        return self.i, (u, i, j, hist_i, sl)


import random 
class DataInputPredict:
    
    def __init__(self, data):
        self.data = data
        self.get_item_set()
        self.ad_size = 100
        
    def get_item_set(self):
        item_list = []
        for t in self.data:
            item_list.extend(t[1])
        self.item_list_candiate = list(set(item_list))
        
    def get_rand_list(self):
        item_candi = random.sample(self.item_list_candiate, self.ad_size-1)
        return item_candi
        
    def get_input(self):
        u_all = []
        i_all = []
        sl_all = []
        hist_all = []
        
        for t in self.data:
            u = [t[0]]*self.ad_size
            item_candi = self.get_rand_list()
            item_candi.append(t[2][0])
            sl = [len(t[1])]*self.ad_size
            hist = np.reshape(t[1]*self.ad_size,[self.ad_size,-1])
            
            u_all.append(u)
            i_all.append(item_candi)
            sl_all.append(sl)
            hist_all.append(hist)
            
        return u_all, i_all, sl_all, hist_all
    
    
            
            
            
        
        
        
        
        






