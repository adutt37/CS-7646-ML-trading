""""""  		  	   		 	 	 			  		 			     			  	 
"""Assess a betting strategy.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	 	 			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		 	 	 			  		 			     			  	 
All Rights Reserved  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Template code for CS 4646/7646  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	 	 			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		 	 	 			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		 	 	 			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		 	 	 			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	 	 			  		 			     			  	 
or edited.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		 	 	 			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		 	 	 			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	 	 			  		 			     			  	 
GT honor code violation.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
-----do not edit anything above this line---  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
Student Name: Tucker Balch (replace with your name)  		  	   		 	 	 			  		 			     			  	 
GT User ID: tb34 (replace with your User ID)  		  	   		 	 	 			  		 			     			  	 
GT ID: 900897987 (replace with your GT ID)  		  	   		 	 	 			  		 			     			  	 
"""  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
import numpy as np
import matplotlib.pyplot as plt 		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def author():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    :return: The GT username of the student  		  	   		 	 	 			  		 			     			  	 
    :rtype: str  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    return "adutt37"  # replace tb34 with your Georgia Tech username.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def gtid():  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    :return: The GT ID of the student  		  	   		 	 	 			  		 			     			  	 
    :rtype: int  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    return 900897987  # replace with your GT ID number  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
def get_spin_result(win_prob):  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
    :param win_prob: The probability of winning  		  	   		 	 	 			  		 			     			  	 
    :type win_prob: float  		  	   		 	 	 			  		 			     			  	 
    :return: The result of the spin.  		  	   		 	 	 			  		 			     			  	 
    :rtype: bool  		  	   		 	 	 			  		 			     			  	 
    """  		  	   		 	 	 			  		 			     			  	 
    result = False  		  	   		 	 	 			  		 			     			  	 
    if np.random.random() <= win_prob:  		  	   		 	 	 			  		 			     			  	 
        result = True  		  	   		 	 	 			  		 			     			  	 
    return result  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			  	 
  		  	   		 	 	 			  		 			     			

# Function to run a single test simulation
def single_test_simulation(probability_of_win):
    max_spins = 1000
    winnings = [0]
    current_winnings = 0

    while current_winnings < 80 and len(winnings) <= max_spins:
        win = False
        bet = 1

        while not win:
            win = get_spin_result(probability_of_win)
            if win:
                current_winnings += bet
            else:
                current_winnings -= bet
                bet *= 2

            winnings.append(current_winnings)

    winnings.extend([current_winnings] * (max_spins + 1 - len(winnings)))
    return np.array(winnings)

# Function to run a realistic simulation with constraints
def simulation_type_2(probability_of_win):
    max_spins = 1000
    max_loss = -256
    winnings = [0]
    current_winnings = 0

    while current_winnings < 80 and current_winnings > max_loss and len(winnings) <= max_spins:
        win = False
        bet = 1

        while not win and len(winnings) <= max_spins:
            win = get_spin_result(probability_of_win)
            if win:
                current_winnings += bet
            else:
                current_winnings -= bet
                bet = min(bet * 2, current_winnings - max_loss)

            winnings.append(current_winnings)

    winnings.extend([current_winnings] * (max_spins + 1 - len(winnings)))
    return np.array(winnings)

# Function to plot figure 1

def plot_figure1(probability_of_win):
    simulations = [single_test_simulation(probability_of_win) for _ in range(10)]
    spins = np.arange(0, 1001)

    for i, sim in enumerate(simulations):
        plt.plot(spins, sim, label=f"Simulation {i+1}")

    plt.title("Spin Number vs Winnings (10 Simulations)")
    plt.xlabel("Spin Number")
    plt.ylabel("Winnings")
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.legend(loc="lower right")
    plt.savefig("images/figure1.png")
    plt.close()

# Function to plot figures 2 and 3

def plot_figures2_and_3(probability_of_win):
    simulations = [single_test_simulation(probability_of_win) for _ in range(1000)]
    spins = np.arange(0, 1001)

    mean = np.mean(simulations, axis=0)
    std_dev = np.std(simulations, axis=0)

    # Plot mean with standard deviation (Figure 2)
    plt.plot(spins, mean, label="Mean")
    plt.plot(spins, mean + std_dev, label="Mean + Std Dev")
    plt.plot(spins, mean - std_dev, label="Mean - Std Dev")
    plt.title("Mean Winnings vs Spins (1000 Simulations)")
    plt.xlabel("Spin Number")
    plt.ylabel("Mean Winnings")
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.legend(loc="lower right")
    plt.savefig("images/figure2.png")
    plt.close()

    # Plot median with standard deviation (Figure 3)
    median = np.median(simulations, axis=0)
    plt.plot(spins, median, label="Median")
    plt.plot(spins, median + std_dev, label="Median + Std Dev")
    plt.plot(spins, median - std_dev, label="Median - Std Dev")
    plt.title("Median Winnings vs Spins (1000 Simulations)")
    plt.xlabel("Spin Number")
    plt.ylabel("Median Winnings")
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.legend(loc="lower right")
    plt.savefig("images/figure3.png")
    plt.close()

# Function to plot figures 4 and 5

def plot_figures4_and_5(probability_of_win):
    simulations = [simulation_type_2(probability_of_win) for _ in range(1000)]
    spins = np.arange(0, 1001)

    mean = np.mean(simulations, axis=0)
    std_dev = np.std(simulations, axis=0)

    # Plot mean with standard deviation (Figure 4)
    plt.plot(spins, mean, label="Mean")
    plt.plot(spins, mean + std_dev, label="Mean + Std Dev")
    plt.plot(spins, mean - std_dev, label="Mean - Std Dev")
    plt.title("Realistic Mean Winnings vs Spins")
    plt.xlabel("Spin Number")
    plt.ylabel("Mean Winnings")
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.legend(loc="lower right")
    plt.savefig("images/figure4.png")
    plt.close()

    # Plot median with standard deviation (Figure 5)
    median = np.median(simulations, axis=0)
    plt.plot(spins, median, label="Median")
    plt.plot(spins, median + std_dev, label="Median + Std Dev")
    plt.plot(spins, median - std_dev, label="Median - Std Dev")
    plt.title("Realistic Median Winnings vs Spins")
    plt.xlabel("Spin Number")
    plt.ylabel("Median Winnings")
    plt.xlim(0, 300)
    plt.ylim(-256, 100)
    plt.legend(loc="lower right")
    plt.savefig("images/figure5.png")
    plt.close()
    
def test_code():
    probability = 0.60  # Probability of a win
    np.random.seed(gtid())  # Seed for reproducibility
    print(get_spin_result(probability))  # Test spin

    # Run experiments and generate figures
    plot_figure1(probability)
    plot_figures2_and_3(probability)
    plot_figures4_and_5(probability)

if __name__ == "__main__":
    test_code()
		  	   		 	 	 			  		 			     			  	 
