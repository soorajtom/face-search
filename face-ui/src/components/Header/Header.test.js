import React from 'react';
import { shallow, render, mount } from 'enzyme';
import Header from './Header';

describe('Header', () => {
  let props;
  let shallowHeader;
  let renderedHeader;
  let mountedHeader;

  const shallowTestComponent = () => {
    if (!shallowHeader) {
      shallowHeader = shallow(<Header {...props} />);
    }
    return shallowHeader;
  };

  const renderTestComponent = () => {
    if (!renderedHeader) {
      renderedHeader = render(<Header {...props} />);
    }
    return renderedHeader;
  };

  const mountTestComponent = () => {
    if (!mountedHeader) {
      mountedHeader = mount(<Header {...props} />);
    }
    return mountedHeader;
  };  

  beforeEach(() => {
    props = {};
    shallowHeader = undefined;
    renderedHeader = undefined;
    mountedHeader = undefined;
  });

  // Shallow / unit tests begin here
 
  // Render / mount / integration tests begin here
  
});
