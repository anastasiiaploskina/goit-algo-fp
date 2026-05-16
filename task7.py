
import random
import matplotlib.pyplot as plt


THEORETICAL_PROBS = {
    2: 1/36,  3: 2/36,  4: 3/36,  5: 4/36,  6: 5/36,  7: 6/36,
    8: 5/36,  9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}


def simulate_dice_rolls(num_rolls):
    counts = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        roll = random.randint(1, 6) + random.randint(1, 6)
        counts[roll] += 1

    probabilities = {sum_value: count / num_rolls for sum_value, count in counts.items()}

    return probabilities


def print_comparison_table(probabilities, num_rolls):
    print(f"\n--- Порівняння для {num_rolls:,} кидків ---")
    print(f"{'Сума':<5} | {'Монте-Карло':<12} | {'Аналітична':<12} | {'Різниця':<10}")
    print("-" * 50)
    for s in range(2, 13):
        mc_p = probabilities[s] * 100
        th_p = THEORETICAL_PROBS[s] * 100
        diff = abs(mc_p - th_p)
        print(f"{s:<5} | {mc_p:<11.2f}% | {th_p:<11.2f}% | {diff:<9.2f}%")
    print("-" * 50)


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках')

    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')

    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        probabilities = simulate_dice_rolls(accuracy)

        print_comparison_table(probabilities, accuracy)

        plot_probabilities(probabilities)
