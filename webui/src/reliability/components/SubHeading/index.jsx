import React from "react";

const SubHeading = (props) => {
  return (
    <div
      style={{
        backgroundColor: "#404040",
        color: "#fff",
        borderRadius: "15px",
        fontSize: "20px",
        textAlign: "center",
        marginBottom: "10px",
      }}
    >
      {props.heading}
    </div>
  );
};

export default SubHeading;
