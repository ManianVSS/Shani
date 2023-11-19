import React from "react";
import { Breadcrumb } from "rsuite";
import AngleRightIcon from "@rsuite/icons/legacy/AngleRight";
import { Link } from "react-router-dom";

const NavLink = React.forwardRef((props, ref) => {
  const { href, as, ...rest } = props;
  return (
    <Link href={href} as={as}>
      <a ref={ref} {...rest} />
    </Link>
  );
});

const BreadcrumbComp = ({ separator }) => {
  return (
    <Breadcrumb separator={separator}>
      <Breadcrumb.Item as={NavLink} href="/">
        Home
      </Breadcrumb.Item>
      <Breadcrumb.Item as={NavLink} href="/components/overview">
        Components
      </Breadcrumb.Item>
      <Breadcrumb.Item active>Breadcrumb</Breadcrumb.Item>
    </Breadcrumb>
  );
};

const BreadcrumbComponent = () => (
  <>
    <BreadcrumbComp separator={<AngleRightIcon />} />
  </>
);

export default BreadcrumbComponent;
