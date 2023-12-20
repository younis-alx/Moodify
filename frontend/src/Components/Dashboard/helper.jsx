import * as React from 'react';
import { BarChart } from '@mui/x-charts/BarChart';
import { axisClasses } from '@mui/x-charts';
import { useTheme } from '@mui/material/styles';
import { ThemeConsumer } from 'styled-components';

const sentimentCount = (all_sentiment) => {
  let positive = 0;
  let negative = 0;
  let neutral = 0;

  all_sentiment.flat().forEach((item) => {
      const highestScoreItem = item.reduce((prev, current) => (prev.score >= current.score) ? prev : current);

      if (highestScoreItem.label === 'Positive') {
          positive++;
      } else if (highestScoreItem.label === 'Negative') {
          negative++;
      } else if (highestScoreItem.label === 'Neutral') {
          neutral++;
      }
  });

  return { positive, negative, neutral };
};

const sentimentArea = (combined_replies) => {
  let areaChartData = []
  combined_replies.forEach((item) => {
      let eachCombo = {}
    //   console.log(JSON.stringify(item, null, 2))
      eachCombo['date'] = new Date(item.created_at).toLocaleDateString('en-US', { month: 'short', day: '2-digit' });
      eachCombo['Positive'] = item.sentiment[0].map((item) => item.label === 'Positive' ? item.score : 0).reduce((a, b) => a + b, 0) * 100;
      eachCombo['Negative'] = item.sentiment[0].map((item) => item.label === 'Negative' ? item.score : 0).reduce((a, b) => a + b, 0) * 100;
      eachCombo['Neutral'] = item.sentiment[0].map((item) => item.label === 'Neutral' ? item.score : 0).reduce((a, b) => a + b, 0) * 100;
      areaChartData.push(eachCombo);
  });
//   console.log(JSON.stringify(areaChartData, null, 2))
  return areaChartData;

  }

  
const SimpleCharts = ({combined_replies}) => {
    const dataset = sentimentArea(combined_replies);
    const theme = useTheme();
    const chartSetting = {
        yAxis: [
          {
            label: 'Score by time',
            fill: theme.palette.mode === 'dark' ? 'rgba(255,255,255,0.12)' : 'rgba(0,0,0,0.12)',
          },
        ],
        width: 400,
        height: 300,
        sx: {
          [`.${axisClasses.left} .${axisClasses.label}`]: {
            transform: 'translate(-20px, 0)',
          },
        },
      };

    return (
      <BarChart
      dataset={dataset}
      xAxis={[{ scaleType: 'band', dataKey: 'date', color: '#FFFFFF'}]}
      series={[
        { dataKey: 'Positive', label: 'Positive' },
        { dataKey: 'Negative', label: 'Negative' },
        { dataKey: 'Neutral', label: 'Neutral' },
      ]}
        {...chartSetting}
        height={300}
        slotProps={
            {
                 legend: 
                 {
                    labelStyle: 
                    {
                        fill: 'white'
                    }
                },
                axisLabel: {
                    fill: 'white',
                    fontWeight: 'thin',

                },
                axisTickLabel: {
                    stroke: 'white',
                    fontWeight: 'thin', 
                },
                
             }
            }
        
            
        
      />
    );
  }

export { sentimentCount, sentimentArea, SimpleCharts };

