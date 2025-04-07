#Welcome! This is a simple chart usng MatPlotLib. - Rose Parker
#_____Imports_____
import matplotlib.pyplot as plt

plt.title("Product Sold")
x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y = [10,25,50,75,100,150,200, 250, 300, 350, 400, 450]
colors = ["red", "pink", "orange", "yellow", "green", "blue", "purple"]

#Plotting the chart
plt.plot(x,y, color="blue", marker="o")
plt.fill_between(x, y, color="red", alpha=0.2)
plt.grid()
plt.legend(["Company Product Sold"])
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart.png")
plt.xlabel("Months")
plt.ylabel("Products Sold")
plt.title("Products Sold")
plt.show()  # Display the chart
#End of code
