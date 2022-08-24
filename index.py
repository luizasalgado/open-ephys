import pyopenephys
import matplotlib.pylab as plt
file = pyopenephys.File("/Users/luizamoreira/Documents/UFABC/IC/Epilepsia/Registros - Cayo/Registro open ephys/NOX2/SE/Camundongo 01 - NOX2 - SE - 2022-06-14_13-50-23")

def analysis(file_name):

    experiments = len(file_name.experiments)
    print('Number of experiments: ', experiments)

    experiment = file_name.experiments[0]
    # recording 1 
    recording = experiment.recordings[0]

    print('Duration: ', recording.duration)
    print('Sampling Rate: ', recording.sample_rate)

    analog_signals = recording.analog_signals
    events_data = recording.events
    spiketrains = recording.spiketrains
    # tracking_data are accessible only using binary format
    tracking_data = recording.tracking

    # plot analog signal of channel 
    signals = analog_signals[0]
    fig_an, ax_an = plt.subplots()
    # ax_an.set_ylim(bottom=100)
    ax_an.plot(signals.times, signals.signal[0])

    # # plot raster for spike trains
    # fig_sp, ax_sp = plt.subplots()
    # for i_s, sp in enumerate(spiketrains):
    #     ax_sp.plot(sp.times, i_s*np.ones(len(sp.times)), '|')

    plt.show()

    return experiments

analysis(file)