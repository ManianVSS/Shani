import React from "react";
import Iframe from "react-iframe";

const IframeComponent = (props) => {
  return (
    <div>
      <Iframe
        url={props.link}
        width={props.width + "px"}
        height={props.height + "px"}
        id="shani-iframe"
        className="shani-iframe"
        display="block"
        position="relative"
      />
    </div>
  );
};

export default IframeComponent;
