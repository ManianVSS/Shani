import React from "react";
import { useParams } from "react-router-dom";

const IndividualReqComponent = (props) => {
  const { requirementid } = useParams();

  return <div>IndividualReqComponent-{requirementid}</div>;
};

export default IndividualReqComponent;
