import React from "react";
import { Card } from "antd";
const { Meta } = Card;

const AntCard = (props) => {
  return (
    <div>
      <Card
        hoverable
        style={{
          width: 240,
        }}
        cover={
          <img
            alt="example"
            src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png"
          />
        }
      >
        <Meta title={props.name} description={props.summary} />
      </Card>
    </div>
  );
};

export default AntCard;
