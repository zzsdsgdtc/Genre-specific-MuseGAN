import numpy as np
import pandas as pd
import pypianoroll
import pretty_midi
import h5py
import tables
import os
           
def main():   
    # This file is used for processing Lakh Matched Dataset with LMD-matched metadata and Lakh Pianoroll Dataset
    # Please download the files from http://hog.ee.columbia.edu/craffel/lmd/lmd_matched.tar.gz
    # and from http://hog.ee.columbia.edu/craffel/lmd/lmd_matched_h5.tar.gz
    # the LPD cleaned dataset can be found here https://drive.google.com/uc?id=1XJ648WDMjRilbhs4hE3m099ZQIrJLvUB&export=download
    # Note to specify the NUM_TO_SELECT and GENRE information in order to construct your own dataset with specific size and genre.
    
    LPD_ROOT = "./lpd_5_cleansed/" 
    LMD_ROOT = "./lmd_matched/" 
    LMD_DATA_ROOT = "./lmd_matched_h5/"
    
    SAVE_PATH = "rock_list.npy" # change it to your saved path
    NUM_TO_SELECT = 600
    GENRE = "rock" # rock, jazz, disco
    
        
    def process_lpd_data(lpd_data_path):
        lpd_data = pypianoroll.load(lpd_data_path)

    def process_lmd_data(lmd_data_path):
        lmd_data = pretty_midi.PrettyMIDI(lmd_data_path)

    def process_lmd_meta_data(lmd_meta_data_path):
        with tables.open_file(lmd_meta_data_path, 'r') as lmd_meta_data:
            terms = lmd_meta_data.root.metadata.artist_terms
            if len(lmd_meta_data.root.metadata.artist_terms_freq) > 0:
                top_term_id = np.argmax(lmd_meta_data.root.metadata.artist_terms_freq)
                top_term = terms[top_term_id]
                top_term_list.append(top_term)
                for x in terms:
                    term_list.append(x)
    count = 0
    def collect_lmd_genre(lmd_meta_data_path, lmd_data_path, genre):
        with tables.open_file(lmd_meta_data_path, 'r') as lmd_meta_data:
            terms = lmd_meta_data.root.metadata.artist_terms
            if len(lmd_meta_data.root.metadata.artist_terms_freq) > 0:
                top_term_id = np.argmax(lmd_meta_data.root.metadata.artist_terms_freq)
                top_term = terms[top_term_id]
                if(top_term == GENRE): 
                    count += 1
                    genre_list.append(lmd_data_path)
                
    term_list = []
    top_term_list = []
    genre_list = []

    for subdir1 in os.listdir(LPD_ROOT):
        path1 = LPD_ROOT + subdir1 + "/"
        for subdir2 in os.listdir(path1):
            path2 = path1 + subdir2 + "/"
            for subdir3 in os.listdir(path2):
                path3 = path2 + subdir3 + "/"
                for lmd_id in os.listdir(path3):
                    path4 = path3 + lmd_id + "/"
                    for lpd_id in os.listdir(path4):
                        lpd_data_path = path4 + lpd_id
                        lmd_data_path = LMD_ROOT + subdir1 + "/" + subdir2 + "/" + subdir3 + "/" + lmd_id + "/" + lpd_id[0:lpd_id.rfind(".")] + ".mid"
                        lmd_meta_data_path = LMD_DATA_ROOT + subdir1 + "/" + subdir2 + "/" + subdir3 + "/" + lmd_id + ".h5" 
                        collect_lmd_genre(lmd_meta_data_path, lmd_data_path, GENRE)
    print("processed a total of " + str(count) + " of files with genre " + GENRE)
    np.save(SAVE_PATH, genre_list[:NUM_TO_SELECT])
    print("saved files to: " + SAVE_PATH + " with " + str(NUM_TO_SELECT) + " songs")
    
if __name__ == '__main__':
    main()