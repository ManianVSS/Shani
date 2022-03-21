import React from "react";
import { useParams } from "react-router-dom";

const IndividualTest = (props) => {
  const { testcaseid } = useParams();
  return <div>IndividualTest-{testcaseid}</div>;
};

export default IndividualTest;
