import React from "react";
import { useParams } from "react-router-dom";

const IndividualDefect = () => {
  const { defectID } = useParams();
  return <div>IndividualDefect-{defectID}</div>;
};

export default IndividualDefect;
