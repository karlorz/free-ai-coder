import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm

print(matplotlib.get_data_path())
print(matplotlib.get_cachedir())

# List of common Chinese fonts to try. Matplotlib will use the first one it finds.
# You might need to install one of these fonts if none are available on your system.
# Common fonts: 'SimHei', 'Microsoft YaHei', 'PingFang SC', 'WenQuanYi Micro Hei', 
# 'Noto Sans CJK SC', 'Source Han Sans SC', 'Arial Unicode MS'
font_names = [
    'SimHei', 'Microsoft YaHei', 'PingFang SC', 'WenQuanYi Micro Hei', 
    'Noto Sans CJK SC', 'Source Han Sans SC', 'Arial Unicode MS'
]
plt.rcParams['font.sans-serif'] = font_names
plt.rcParams['axes.unicode_minus'] = False  # Resolve a problem with the display of the minus sign

# --- Font Debugging ---
# Uncomment the following lines to print information about available fonts
# print("--- Font Debugging Information ---")
# print(f"Matplotlib is trying these fonts for sans-serif: {plt.rcParams['font.sans-serif']}")
#
# available_fonts = sorted(set([f.name for f in fm.fontManager.ttflist]))
# print("\nAvailable system fonts recognized by Matplotlib:")
# for font_name in available_fonts:
#     print(font_name)
#
# print("\nChecking if any of the preferred fonts are available:")
# found_fonts = []
# for preferred_font in font_names:
#    if preferred_font in available_fonts:
#        found_fonts.append(preferred_font)
# if found_fonts:
#    print(f"Found the following preferred fonts on your system: {found_fonts}")
# else:
#    print("None of the preferred Chinese fonts were found. You may need to install one.")
# print("--- End Font Debugging Information ---")

# Data for plotting
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Create a plot
plt.plot(x, y)

# Add title and labels with Chinese characters
plt.title("测试标题")  # 测试标题
plt.xlabel("X轴 - 测试")  # X轴 - 测试
plt.ylabel("Y轴 - 测试")  # Y轴 - 测试

# Display the plot
plt.show()
