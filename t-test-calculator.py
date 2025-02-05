from scipy import stats

def calculate_p_value():
    try:
        # Get user input
        t_score = float(input("Enter t-score: "))
        df = int(input("Enter degrees of freedom (df): "))
        
        # Calculate two-tailed p-value
        p_value = stats.t.sf(abs(t_score), df) * 2
        
        # Print results with formatting
        print("\nResults:")
        print(f"t-score: {t_score:.4f}")
        print(f"Degrees of freedom: {df}")
        print(f"p-value (two-tailed): {p_value:.4f}")
        
        # Interpret statistical significance
        if p_value < 0.001:
            print("Result is highly statistically significant (p < 0.001)")
        elif p_value < 0.01:
            print("Result is very statistically significant (p < 0.01)")
        elif p_value < 0.05:
            print("Result is statistically significant (p < 0.05)")
        else:
            print("Result is not statistically significant (p ≥ 0.05)")
            
    except ValueError:
        print("Error: Please enter valid numerical values.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("T-Test P-Value Calculator")
    print("-------------------------")
    calculate_p_value()
