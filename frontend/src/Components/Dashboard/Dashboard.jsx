import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
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
    Flex,
} from "@tremor/react";
import { sentimentCount, SimpleCharts } from './helper';
import SalesPeopleTable from "./Table";
import SummaryTable from "./summary";


export default function Dashboard() {
    const location = useLocation();
    const data = location.state?.data;
    let all_sentiment = [];
    if (data?.combined_replies) {
        all_sentiment = data.combined_replies.map((item) => item.sentiment);
    }

    useEffect(() => {
        if (data?.combined_replies) {
            all_sentiment = data.combined_replies.map((item) => item.sentiment);
        }
    }, [data]);
    
    // console.log(JSON.stringify(areaChartData, null, 2));
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
            <TabPanel >
                <Grid  numItemsMd={2} numItemsLg={2} className="gap-4 mt-4 justify-center max-w-[64rem] mx-auto">
                <Card className="max-w-lg mx-auto ">
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
                    <Text className="text-center mt-6">Total Tweets: {data?.combined_replies.length}</Text>
                    <Flex className="justify-center gap-6">
                    <Title className="text-center mt-6">Positive: {Math.floor((sentimentCount(all_sentiment).positive/data?.replies_count) * 100)}%</Title>
                    <Title className="text-center mt-6">Neutral: {Math.floor((sentimentCount(all_sentiment).neutral/data?.replies_count) * 100)}%</Title>
                    <Title className="text-center mt-6">Negative: {Math.floor((sentimentCount(all_sentiment).negative/data?.replies_count) * 100)}%</Title>
                    </Flex>
                </Card>
                <Card className="max-w-lg mx-auto">
                    <div className="h-27" >
                    <Title className="text-center">Sentiment Area Overview</Title>
                    </div>
                    <SimpleCharts all_sentiment={all_sentiment} combined_replies={data.combined_replies}/>
                </Card>

                </Grid>
                <div className="mt-4">
                <Card className="max-w-[64rem] mx-auto">
                    <SummaryTable combined_replies={data?.combined_replies}/>
                    <div className="h-75" />
                </Card>
                </div>
            </TabPanel>
            <TabPanel>
                <div className="mt-6">
                <Card>
                    <SalesPeopleTable combined_replies={data?.combined_replies}/>
                    <div className="h-95" />
                </Card>
                </div>
            </TabPanel>
            </TabPanels>
        </TabGroup>
        </main>
    </>
  );
}