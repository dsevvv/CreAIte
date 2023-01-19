import { UIEvent, PhotoEditorSDKUI } from "photoeditorsdk";
import React from 'react';

export class PhotoEditorSDK extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      templateImage: props.templateImage,
      editableImage: props.editableImage
    };
  }

  componentDidMount() {
    this.initEditor();
  }

  async initEditor() {
    const editor = await PhotoEditorSDKUI.init({
      container: "#editor",
      image: this.state.templateImage,
      // Please replace this with your license: https://img.ly/dashboard
      license: '',
    });

    editor.addImage({
      src: this.state.editableImage,
      x: 0,
      y: 0,
      draggable: true,
    });

    console.log("PhotoEditorSDK for Web is ready!");
    editor.on(UIEvent.EXPORT, (imageSrc) => {
      console.log("Exported ", imageSrc);
    });
  }

  render() {
    return (
      <div
        id="editor"
        style={{ width: "100vw", height: "100vh" }}
      />
    );
  }
}