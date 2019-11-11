from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
df_goals = pd.read_csv('goals.csv')

df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']

sns.set_style('whitegrid')
sns.set_context('notebook')
f, ax = plt.subplots(figsize=(12,7))
ax = sns.barplot( data=df, x='Year', y='Total Goals')

ax.set_title('Average Number of Goals Scores in World Cup Matches By Year')

plt.savefig('avg_goalsBars.png')

f, ax2 = plt.subplots(figsize=(12,7))
ax2 = sns.boxplot(x='year', y='goals', data=df_goals, palette='Spectral')
ax2.set_title('Goals Visualization')

plt.savefig('goalsvisualization.png')