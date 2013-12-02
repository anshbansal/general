package aseemDao;

import java.sql.Connection;
import java.sql.SQLException;

import aseemEnums.TableName;

public interface DAOInsert {

	public abstract <T> boolean putInto(Connection con, TableName tableName,
			T currentPojo, boolean running) throws SQLException;
}
