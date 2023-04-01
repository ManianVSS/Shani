import React from "react";
import { NewsHeaderCard } from "react-ui-cards";

export const CardItem001 = (props) => (
  <NewsHeaderCard thumbnail={props.image} tags={[props.summary]} />
);
