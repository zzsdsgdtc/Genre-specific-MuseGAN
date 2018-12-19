import numpy as np

def main():
    # file_path = 'train_x_lpd_5_phr.npz'
    # with np.load(file_path) as f:
    #     data = np.zeros(f['shape'], np.bool_)
    #     data[[x for x in f['nonzero']]] = True 

    # data_train_r = data[:6000, :, :, :, :]
    # data_valid_r = data[6000:7000, :, :, :, :]
    # data_test_r = data[7000:8000, :, :, :, :]
    predix = ['Bass','Drums', 'Guitar', 'Piano', 'Strings']

    # rock music 
    train_path = './data_phr_rock/tra'
    # valid_path = './data_phr_rock/val'
    # test_path = './data_phr_rock/test'

    predix = ['Bass','Drums', 'Guitar', 'Piano', 'Strings']

    data_temp = np.load(train_path + '/' + 'Drums.npy') 
    data_train_r = np.zeros((data_temp.shape[0], data_temp.shape[1], data_temp.shape[2], data_temp.shape[3], 5))
    for i in range(len(predix)):
        data_train_r[:,:,:,:,i] = np.load(train_path + '/' + predix[i] + '.npy')
    # np.savez("data_train_jazz.npz", data_train_j)
#     print data_train_j

#     data_temp = np.load(valid_path + '/' + 'Drums.npy') 
#     data_valid_r = np.zeros((data_temp.shape[0], data_temp.shape[1], data_temp.shape[2], data_temp.shape[3], 5))
#     for i in range(len(predix)):
#         data_valid_r[:,:,:,:,i] = np.load(valid_path + '/' + predix[i] + '.npy')
# #     print data_valid_j.shape
#     # np.save("data_val_jazz.npy", data_valid_j)

#     data_temp = np.load(test_path + '/' + 'Drums.npy') 
#     data_test_r = np.zeros((data_temp.shape[0], data_temp.shape[1], data_temp.shape[2], data_temp.shape[3], 5))
#     for i in range(len(predix)):
#         data_test_r[:,:,:,:,i] = np.load(test_path + '/' + predix[i] + '.npy')
# #     print data_test_j.shape
#     #np.save("data_test_jazz.npy", data_test_j)
#     data_rock = np.concatenate((data_train_r,data_valid_r,data_test_r))
    data_rock = data_train_r
    
    # jazz music 
    train_path = './data_phr_jazz/tra'
    valid_path = './data_phr_jazz/val'
    test_path = './data_phr_jazz/test'

    data_temp = np.load(train_path + '/' + 'Drums.npy') 
    data_train_j = np.zeros((data_temp.shape[0], data_temp.shape[1], data_temp.shape[2], data_temp.shape[3], 5))
    for i in range(len(predix)):
        data_train_j[:,:,:,:,i] = np.load(train_path + '/' + predix[i] + '.npy')
    # np.savez("data_train_jazz.npz", data_train_j)
#     print data_train_j

    data_temp = np.load(valid_path + '/' + 'Drums.npy') 
    data_valid_j = np.zeros((data_temp.shape[0], data_temp.shape[1], data_temp.shape[2], data_temp.shape[3], 5))
    for i in range(len(predix)):
        data_valid_j[:,:,:,:,i] = np.load(valid_path + '/' + predix[i] + '.npy')
#     print data_valid_j.shape
    # np.save("data_val_jazz.npy", data_valid_j)

    data_temp = np.load(test_path + '/' + 'Drums.npy') 
    data_test_j = np.zeros((data_temp.shape[0], data_temp.shape[1], data_temp.shape[2], data_temp.shape[3], 5))
    for i in range(len(predix)):
        data_test_j[:,:,:,:,i] = np.load(test_path + '/' + predix[i] + '.npy')
#     print data_test_j.shape
    #np.save("data_test_jazz.npy", data_test_j)
    data_jazz = np.concatenate((data_train_j,data_valid_j,data_test_j))

    # disco music 
    train_path_d = './data_phr_disc/tra'
    valid_path_d = './data_phr_disc/val'
    test_path_d = './data_phr_disc/test'


    data_temp = np.load(train_path_d + '/' + 'Drums.npy') 
    data_train_d = np.zeros((data_temp.shape[0], data_temp.shape[1], data_temp.shape[2], data_temp.shape[3], 5))
    for i in range(len(predix)):
        data_train_d[:,:,:,:,i] = np.load(train_path_d + '/' + predix[i] + '.npy')
    # np.savez("data_train_disco.npz", data_train_d)
#     print data_train_d.shape

    data_temp = np.load(valid_path + '/' + 'Drums.npy') 
    data_valid_d = np.zeros((data_temp.shape[0], data_temp.shape[1], data_temp.shape[2], data_temp.shape[3], 5))
    for i in range(len(predix)):
        data_valid_d[:,:,:,:,i] = np.load(valid_path + '/' + predix[i] + '.npy')
    #np.save("data_val_disco.npy", data_valid_d)
#     print data_valid_d.shape

    data_temp = np.load(test_path + '/' + 'Drums.npy') 
    data_test_d = np.zeros((data_temp.shape[0], data_temp.shape[1], data_temp.shape[2], data_temp.shape[3], 5))
    for i in range(len(predix)):
        data_test_d[:,:,:,:,i] = np.load(test_path + '/' + predix[i] + '.npy')
    #np.save("data_test_disco.npy", data_test_d)
#     print data_test_d.shape

    data_disco = np.concatenate((data_train_d,data_valid_d,data_test_d))



    train_X = np.zeros((data_jazz.shape[0] + data_rock.shape[0] + data_disco.shape[0],  4, 48, 84, 5))
    train_X[:data_jazz.shape[0], : , :, :, :] = data_jazz[:,:,:,24:108,:]
    train_X[data_jazz.shape[0] : (data_jazz.shape[0] + data_rock.shape[0]), : , :, :, :] = data_rock[:,:,:,24:108,:]
    train_X[(data_jazz.shape[0] + data_rock.shape[0]):, : , :, :, :] = data_disco[:,:,:,24:108,:]

    def _get_label_pair(label):
        true = [0, 0, 0]
        true[label] = 1
        wrong = [0, 0, 0]
        wrong[np.random.choice([i for i in range(3) if i != label])] = 1
        return np.array((true, wrong))

    train_y = np.zeros((data_jazz.shape[0] + data_rock.shape[0] + data_disco.shape[0], 3))
    train_y_w = np.zeros((data_jazz.shape[0] + data_rock.shape[0] + data_disco.shape[0], 3))
    for i in range(data_jazz.shape[0]):
        p = _get_label_pair(0)
        train_y[i] = p[0]
        train_y_w[i] = p[1]
    for i in range(data_jazz.shape[0], data_jazz.shape[0] + data_rock.shape[0]):
        p = _get_label_pair(1)
        train_y[i] = p[0]
        train_y_w[i] = p[1]
    for i in range(data_jazz.shape[0] + data_rock.shape[0], len(train_y)):
        p = _get_label_pair(2)
        train_y[i] = p[0]
        train_y_w[i] = p[1]

    l = [i for i in range(len(train_y))]
    np.random.shuffle(l)
    train_X = train_X[l]
    train_y = train_y[l]
    train_y_w = train_y_w[l]
    np.savez_compressed('data.npz', shape = train_X.shape, nonzero = np.nonzero(train_X))
    np.save('label.npy', train_y)
    np.save('label_w.npy', train_y_w)

if __name__ == "__main__":
    main()