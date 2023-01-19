import React from 'react';
import './index.css';
import CreativeEditorSDK from '@cesdk/cesdk-js';
import { useRef, useEffect } from 'react';

const Component = (props = {}) => {
  const cesdk_container = useRef(null);

  useEffect(() => {
    if (cesdk_container.current) {
      const config = {
        images: [
          {
            src: props.templateImage,
            x: 0,
            y: 0,
            draggable: false,
          },
          {
            src: props.editableImage,
            x: 0,
            y: 0,
            draggable: true,
          },
        ],
      };
      CreativeEditorSDK.init(cesdk_container.current, config).then(
        (instance) => {
          /** do something with the instance of CreativeEditor SDK **/
        }
      );
    }
  }, [props, cesdk_container]);


  return (
    <div
      ref={cesdk_container}
      style={{ width: '100vw', height: '100vh' }}
    ></div>
  );
};

export default Component;
