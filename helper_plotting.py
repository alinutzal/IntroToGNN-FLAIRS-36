# imports from installed libraries
import os
import matplotlib.pyplot as plt
import numpy as np
import torch

def plot_training_loss(loss_list, num_epochs, iter_per_epoch,
                       results_dir=None):

    plt.figure()
    ax1 = plt.subplot(1, 1, 1)
    ax1.plot(range(len(loss_list)),
             (loss_list), label='Loss')

    if len(loss_list) > 1000:
        ax1.set_ylim([
            0, np.max(loss_list[1000:])*1.5
            ])

    #newlabel = list(range(num_epochs+1))

    #newpos = [e*iter_per_epoch for e in newlabel]

    #ax1.set_xticks(newpos[::50])
    #ax1.set_xticklabels(newlabel[::50])

    #ax1.xaxis.set_ticks_position('bottom')
    #ax1.xaxis.set_label_position('bottom')
    #ax1.spines['bottom'].set_position(('outward', 45))
    #ax1.set_xlabel('Epochs')
    #ax1.set_xlim(ax1.get_xlim())
    ###################

    plt.tight_layout()

    if results_dir is not None:
        image_path = os.path.join(results_dir, 'plot_training_loss.pdf')
        plt.savefig(image_path)
    return
        
