import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from scipy import stats

class TTestCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("T-Test P-Value Calculator")
        self.root.geometry("400x500")
        
        # Create and set up the main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Input fields
        ttk.Label(self.main_frame, text="T-Score:").grid(row=0, column=0, pady=5, sticky=tk.W)
        self.t_score = ttk.Entry(self.main_frame, width=20)
        self.t_score.grid(row=0, column=1, pady=5, padx=5)
        
        ttk.Label(self.main_frame, text="Degrees of Freedom:").grid(row=1, column=0, pady=5, sticky=tk.W)
        self.df = ttk.Entry(self.main_frame, width=20)
        self.df.grid(row=1, column=1, pady=5, padx=5)
        
        # Test type selection
        ttk.Label(self.main_frame, text="Test Type:").grid(row=2, column=0, pady=5, sticky=tk.W)
        self.test_type = tk.StringVar(value="two")
        ttk.Radiobutton(self.main_frame, text="Two-tailed", variable=self.test_type, 
                       value="two").grid(row=2, column=1, sticky=tk.W)
        ttk.Radiobutton(self.main_frame, text="One-tailed", variable=self.test_type, 
                       value="one").grid(row=3, column=1, sticky=tk.W)
        
        # Calculate button
        ttk.Button(self.main_frame, text="Calculate", 
                  command=self.calculate).grid(row=4, column=0, columnspan=2, pady=20)
        
        # Results display
        self.result_frame = ttk.LabelFrame(self.main_frame, text="Results", padding="10")
        self.result_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        self.p_value_label = ttk.Label(self.result_frame, text="")
        self.p_value_label.grid(row=0, column=0, sticky=tk.W)
        
        self.significance_label = ttk.Label(self.result_frame, text="")
        self.significance_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        
    def calculate(self):
        try:
            t_score = float(self.t_score.get())
            df = int(self.df.get())
            
            # Calculate p-value based on test type
            if self.test_type.get() == "two":
                p_value = stats.t.sf(abs(t_score), df) * 2
                test_type_text = "two-tailed"
            else:
                p_value = stats.t.sf(abs(t_score), df)
                test_type_text = "one-tailed"
            
            # Update results display
            self.p_value_label.config(
                text=f"p-value ({test_type_text}): {p_value:.4f}")
            
            # Interpret significance
            if p_value < 0.001:
                sig_text = "Result is highly statistically significant (p < 0.001)"
            elif p_value < 0.01:
                sig_text = "Result is very statistically significant (p < 0.01)"
            elif p_value < 0.05:
                sig_text = "Result is statistically significant (p < 0.05)"
            else:
                sig_text = "Result is not statistically significant (p ≥ 0.05)"
            
            self.significance_label.config(text=sig_text)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = TTestCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
