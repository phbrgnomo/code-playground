import re

# Example lines
line1 = "12,50% Recebíveis KNCR11 COMPRA Kinea Rendimentos 5.812 102 101 101% 0,5% 16,8% 13,0%"
line2 = "10.0% Recebív eis RZAK11 Riza Akin F undo De Inv estiment o Imobiliário - Fii"

# Regex pattern to match the lines
line_pattern = re.compile(r'(\d+(?:,\d{1,3})*(?:\.\d+)?)% .*?([A-Za-z]+[1-9]\d*(?:\d{2})?)\b.*?(?:\n|$)')

# Find matches in the lines
matches_line1 = line_pattern.findall(line1)
matches_line2 = line_pattern.findall(line2)

# Print the matches
print("Matches for Line 1:", matches_line1)
print("Matches for Line 2:", matches_line2)
