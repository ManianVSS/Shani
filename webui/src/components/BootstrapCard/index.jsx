import React from "react";
import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";

const BootstrapCard = (props) => {
  return (
    <div>
      <Card style={{ width: "18rem", marginBottom: "5px" }}>
        {/* <Card.Img variant="top" src="holder.js/100px180?text=Image cap" /> */}
        <Card.Body>
          <Card.Title>{props.name}</Card.Title>
          <Card.Text>{props.summary}</Card.Text>
        </Card.Body>
        <ListGroup className="list-group-flush">
          <Card.Text>{props.name}</Card.Text>
          <Card.Text>{props.name}</Card.Text>
          <Card.Text>{props.name}</Card.Text>
        </ListGroup>
        <Card.Body>
          <Card.Link href="#">Card Link</Card.Link>
          <Card.Link href="#">Another Link</Card.Link>
        </Card.Body>
      </Card>
    </div>
  );
};

export default BootstrapCard;
