fig2 = plt.figure(2)

# ??????
code_result, tempZ = feedforward(w[0], b[0], X[0])

# ???????
for iImg in range(nColumn):
    ax = plt.subplot(2, nColumn, iImg+1)
    plt.imshow(unlabeled_data[:,eachDigitNum * iImg + 1].reshape((width,height)).T, cmap= plt.cm.gray)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

# ?????????
for iImg in range(nColumn):
    ax = plt.subplot(2,nColumn,iImg+nColumn+1)
    plt.imshow(code_result[:,eachDigitNum * iImg + 1].reshape((hidden_node,1)), cmap=plt.cm.gray)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
