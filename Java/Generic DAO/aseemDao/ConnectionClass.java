package aseemDao;

import java.sql.Connection;
import java.sql.SQLException;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.sql.DataSource;

import aseemEnums.Databases;

public class ConnectionClass {
	public static final Databases DATABASE_CODE = Databases.Oracle;

	private DataSource ds;

	public ConnectionClass() throws NamingException {
		Context ctx = new InitialContext();
		switch (DATABASE_CODE) {
		case Oracle:
			this.ds = (DataSource) ctx
					.lookup("java:/comp/env/jdbc/OracleSource");
			break;
		default:
		}
	}

	public Connection getConnection() throws SQLException {
		Connection con = ds.getConnection();
		con.setAutoCommit(false);
		return con;
	}

	public void rollBackAndClose(Connection con) throws SQLException {
		con.rollback();
		con.close();
	}

	public void commitAndClose(Connection con) throws SQLException {
		con.commit();
		con.close();
	}

}
