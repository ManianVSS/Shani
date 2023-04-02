import React from "react";
import { Button, Card } from "react-bootstrap";

const CardItem003 = (props) => {
  return (
    <div>
      <Card className="bg-dark text-white">
        <Card.Img
          src={props.image}
          alt="Card image"
          style={{ width: "300px" }}
        />
        <Card.ImgOverlay>
          <Card.Title
            style={{
              textAlign: "center",
              fontWeight: "bold",
              border: "1px solid #404040",
              borderRadius: "15px",
              background: "#404040",
            }}
          >
            {props.name}
          </Card.Title>
          <Card.Text
            style={{
              textAlign: "center",
              background: "white",
              color: "#404040",
              border: "1px solid white",
              borderRadius: "10px",
            }}
          >
            {props.description}
          </Card.Text>
          {/* <Card.Text>Last updated 3 mins ago</Card.Text> */}
          <div
            style={{
              textAlign: "center",
              position: "absolute",
              bottom: "10px",
              right: "37%",
              background: "#666666",
              border: "1px solid #666666",
              borderRadius: "10px",
            }}
          >
            <Button variant="primary">Launch</Button>
          </div>
        </Card.ImgOverlay>
      </Card>
    </div>
  );
};

export default CardItem003;
