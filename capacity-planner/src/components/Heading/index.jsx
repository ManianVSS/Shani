import React from "react";

const Heading = (props) => {
  return (
    <div
      style={{
        backgroundColor: "#228be6",
        color: "#fff",
        borderRadius: "15px",
        fontSize: "25px",
        textAlign: "center",
        marginBottom: "10px",
      }}
    >
      {props.heading}
    </div>
  );
};

export default Heading;
