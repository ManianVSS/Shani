import React from "react";
import DocViewer, { DocViewerRenderers } from "react-doc-viewer";

const Documentation = () => {
  const docs = [
    // { uri: "https://url-to-my-pdf.pdf" },
    { uri: require("../../data/documents/BASICSOFTHEUNIVERSE.pdf") },
    { uri: require("../../data/documents/sample-xlsx.xlsx") },
    { uri: require("../../data/documents/Sample-word-file.docx") },
  ];
  return <DocViewer pluginRenderers={DocViewerRenderers} documents={docs} />;
};

export default Documentation;
