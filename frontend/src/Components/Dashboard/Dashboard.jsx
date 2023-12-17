import { useLocation } from "react-router-dom";

import {
    Card,
    Grid,
    Tab,
    TabGroup,
    TabList,
    TabPanel,
    TabPanels,
    Text,
    Title,
    DonutChart,
    Flex
} from "@tremor/react";

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

      
export default function Dashboard() {
    const location = useLocation();
    const data = location.state?.data;
    let all_sentiment;
    if (data?.combined_replies) {
        all_sentiment = data.combined_replies.map((item) => item.sentiment);
    }
    
    console.log(JSON.stringify(data.combined_replies, null, 2)) // TODO: create the second tab from using created_at at x-axis and sentiment score at y-axis :)
  return (
    <>
        <main className="p-12 appear">
        <Title style={{color: 'black'}}>Dashboard</Title>
        <Text>Tweet and Replies Sentiment analysis</Text>

        <TabGroup className="mt-6">
            <TabList>
            <Tab>Overview</Tab>
            <Tab>Detail</Tab>
            </TabList>
            <TabPanels>
            <TabPanel>
                <Grid numItemsMd={2} numItemsLg={2} className="gap-6 mt-6">
                <Card className="max-w-lg mx-auto">
                    <div className="h-27">
                    <Title className="text-center">Sentiment Pie Overview</Title>
                    </div>
                    <DonutChart
                        className="mt-6"
                        data={
                            [
                                { label: "Positive", score: sentimentCount(all_sentiment).positive},
                                { label: "Neutral", score: sentimentCount(all_sentiment).neutral},
                                { label: "Negative", score: sentimentCount(all_sentiment).negative}
                            ]
                        }
                        category="score"
                        variant="pie"
                        index="label"
                        showAnimation={true}
                        
                        colors={["cyan",  "slate", "red"]}
                    />
                </Card>
                <Card>
                    {/* Placeholder to set height */}
                    <div className="h-28" />
                </Card>

                </Grid>
                <div className="mt-6">
                <Card>
                    <div className="h-80" />
                </Card>
                </div>
            </TabPanel>
            <TabPanel>
                <div className="mt-6">
                <Card>
                    <div className="h-96" />
                </Card>
                </div>
            </TabPanel>
            </TabPanels>
        </TabGroup>
        </main>
    </>
  );
}