import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link } from 'react-router-dom';
import styles from './Calendar.css';
import routes from '../../constants/routes.json';

import { Card, Col, Row } from 'antd';
const { Meta } = Card;

import { Layout, Menu, Breadcrumb } from 'antd';

const { Header, Content, Footer } = Layout;

import games from './ns.json';

export default function Calendar() {
  return (
    <Layout className="layout">
      <Header>
        <div className="logo" />
        <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
          <Menu.Item key="1">nav 1</Menu.Item>
          <Menu.Item key="2">nav 2</Menu.Item>
          <Menu.Item key="3">nav 3</Menu.Item>
        </Menu>
      </Header>

      <Content style={{ padding: '0 50px' }}>
        <div className="site-layout-content">
          <div className="site-card-wrapper">
            <Row gutter={[16, 16]}>
              {games.map((post, i) => (
                <Col key={i} span={6} >
                  <Card
                    hoverable
                    style={{ width: 240 }}
                    cover={<img alt="example" src={post.minipic} />}
                  >
                    <Meta title={post.name} description={post.date} />
                  </Card>
                </Col>
              ))}
            </Row>
          </div>
        </div>
      </Content>

      <Footer style={{ textAlign: 'center' }}>vgm ©2021 Created with ♥️ by Sree in 🇦🇺</Footer>
    </Layout>
  );
}
