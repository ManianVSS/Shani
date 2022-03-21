import React from "react";
import { useParams } from "react-router-dom";

const IndividualUsecase = (props) => {
  const { usecaseid } = useParams();
  return <div>IndividualUsecase-{usecaseid}</div>;
};

export default IndividualUsecase;
