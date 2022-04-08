import {
  FaBook,
  FaChartPie,
  FaLightbulb,
  FaTicketAlt,
  FaUsers,
  FaUserTie,
} from "react-icons/fa";
export const menuData = [
  {
    title: "Overview",
    icon: <FaChartPie style={{ marginRight: "0.5rem" }} />,
    url: "/",
  },
  {
    title: "Requirements",
    icon: <FaBook style={{ marginRight: "0.5rem" }} />,
    url: "/requirements",
  },
  {
    title: "Use Cases",
    icon: <FaTicketAlt style={{ marginRight: "0.5rem" }} />,
    url: "/usecases",
  },
  {
    title: "Test Cases",
    icon: <FaLightbulb style={{ marginRight: "0.5rem" }} />,
    url: "/testcases",
  },
  {
    title: "Use case categories",
    icon: <FaUsers style={{ marginRight: "0.5rem" }} />,
    url: "/features",
  },
  {
    title: "Runs",
    icon: <FaTicketAlt style={{ marginRight: "0.5rem" }} />,
    url: "/runs",
  },
  {
    title: "Execution Records",
    icon: <FaBook style={{ marginRight: "0.5rem" }} />,
    url: "/executionrecords",
  },
];

export const tableTitles = [
  "id",
  "name",
  "Modality score",
  "Serviceability score",
  "Test Confidence",
  "Development Confidence",
  "Readinesss",
  "Weightage",
];
export const data = [
  ["Contact Email not Linked", "Tom Cruise", "May 26, 2019", "High"],
  ["Adding Images to Featured Posts", "Matt Damon", "May 26, 2019", "low"],
  [
    "When will I be charged this month?",
    "Robert Downey",
    "May 26, 2019",
    "High",
  ],
  ["Payment not going through", "Christian Bale", "May 25, 2019", "Normal"],
  ["Unable to add replies", "Henry Cavil", "May 26, 2019", "High"],
];
