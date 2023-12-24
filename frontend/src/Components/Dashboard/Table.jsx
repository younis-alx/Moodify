import { InformationCircleIcon } from "@heroicons/react/solid";
import {
  BadgeDelta,
  Flex,
  Icon,
  MultiSelect,
  MultiSelectItem,
  Select,
  SelectItem,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeaderCell,
  TableRow,
  Title,
} from "@tremor/react";
import { useState } from "react";

import { v4 as uuid4 } from "uuid";

const deltaTypes = {
  Neutral: "unchanged",
  Positive: "moderateIncrease",
  Negative: "moderateDecrease",
};

export default function SalesPeopleTable({ combined_replies }) {
  const [selectedStatus, setSelectedStatus] = useState("all");
  const [selectedNames, setSelectedNames] = useState([]);
  const relavantData = combined_replies.map(item => {
      return {
          name: item.user_replies.user_name,
          id : uuid4(),
          tweet_id: item.tweet_id,
          Postive: item.sentiment.flat().map((item) => item.label === 'Positive' ? item.score : 0).reduce((a, b) => a + b, 0) * 100,
          Negative: item.sentiment.flat().map((item) => item.label === 'Negative' ? item.score : 0).reduce((a, b) => a + b, 0) * 100,
          Neutral: item.sentiment.flat().map((item) => item.label === 'Neutral' ? item.score : 0).reduce((a, b) => a + b, 0) * 100,
          date: item.created_at,
          text: item.reply_text,
          reply_to_tweet: item.reply_to_tweet_id,
          location: item.user_replies.location || 'unknown',
          status: item.sentiment.flat().reduce((prev, current) => (prev.score >= current.score) ? prev : current).label
        }
    })
    console.log(JSON.stringify(relavantData, null, 2));
  const isSalesPersonSelected = (salesPerson) =>
    (salesPerson.status === selectedStatus || selectedStatus === "all") &&
    (selectedNames.includes(salesPerson.name) || selectedNames.length === 0);

  return (
    <>
      <div>
        <Flex className="space-x-0.5" justifyContent="start" alignItems="center">
          <Title> Performance History </Title>
          <Icon
            icon={InformationCircleIcon}
            variant="simple"
            tooltip="Shows Sentiment Analysis of Tweets and Replies"
          />
        </Flex>
      </div>
      <div className="flex space-x-2">
        <MultiSelect
          className="max-w-full sm:max-w-xs"
          onValueChange={setSelectedNames}
          placeholder="Select name..."
        >
          {relavantData.map((item) => (
            <MultiSelectItem key={item.id} value={item.name}>
              {item.name}
            </MultiSelectItem>
          ))}
        </MultiSelect>
        <Select
          className="max-w-full sm:max-w-xs"
          defaultValue="all"
          onValueChange={setSelectedStatus}
        >
          <SelectItem value="all">All Performances</SelectItem>
          <SelectItem value="Positive">Overperforming</SelectItem>
          <SelectItem value="Neutral">Average</SelectItem>
          <SelectItem value="Negative">Underperforming</SelectItem>
        </Select>
      </div>
        <div className="max-h-96 overflow-y-auto">

            <Table className="mt-6">
                <TableHead>
                <TableRow className="mt-6">
                    <TableHeaderCell>Name</TableHeaderCell>
                    <TableHeaderCell className="text-right">Positive Score(%)</TableHeaderCell>
                    <TableHeaderCell className="text-right">Negative Score(%)</TableHeaderCell>
                    <TableHeaderCell className="text-right">Neutral Score (%)</TableHeaderCell>
                    <TableHeaderCell className="text-right">Location</TableHeaderCell>
                    <TableHeaderCell className="text-right">Text</TableHeaderCell>
                    <TableHeaderCell className="text-right">Status</TableHeaderCell>
                </TableRow>
                </TableHead>

                <TableBody>
                    
                {relavantData
                    .filter((item) => isSalesPersonSelected(item))
                    .map((item) => (
                        <TableRow key={item.id} className="">
                        <TableCell>{item.name}</TableCell>
                        <TableCell className="text-right">{parseFloat(item.Postive).toFixed(2)}</TableCell>
                        <TableCell className="text-right">{parseFloat(item.Negative).toFixed(2)}</TableCell>
                        <TableCell className="text-right">{parseFloat(item.Neutral).toFixed(2)}</TableCell>
                        <TableCell className="text-right">{item.location}</TableCell>
                        <TableCell className="text-right whitespace-normal">{item.text}</TableCell>
                        <TableCell className="text-right">
                        <BadgeDelta deltaType={deltaTypes[item.status]} size="xs">
                            {item.status}
                        </BadgeDelta>
                        </TableCell>
                    </TableRow>
                    ))}
                </TableBody>
            </Table>
        </div>
    </>
  );
}