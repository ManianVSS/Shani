import React from "react";
import { Card, Title, Text, Tab, TabList, ColGrid, Block } from "@tremor/react";

import { useState } from "react";
import TremorCards from "../../components/DashboardComponents/TremorCards";
import FirstContainer from "../../components/DashboardComponents/FirstContainer";
import SecondContainer from "../../components/DashboardComponents/SecondContainer";

const Dashboard = () => {
  const [selectedView, setSelectedView] = useState(1);
  return (
    <main>
      <Title>Dashboard</Title>
      <Text>Sales and growth stats for anonymous inc.</Text>
      <TabList
        defaultValue={1}
        handleSelect={(value) => setSelectedView(value)}
        marginTop="mt-6"
      >
        <Tab value={1} text="Page 1" />
        <Tab value={2} text="Page 2" />
      </TabList>

      {selectedView === 1 ? (
        <>
          <TremorCards />
          <FirstContainer />
        </>
      ) : (
        <SecondContainer />
      )}
    </main>
  );
};

export default Dashboard;
